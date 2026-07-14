import json
import boto3
import streamlit as st


def get_b2_client():
    return boto3.client(
        "s3",
        endpoint_url=st.secrets["B2_ENDPOINT"],
        aws_access_key_id=st.secrets["B2_KEY_ID"],
        aws_secret_access_key=st.secrets["B2_APPLICATION_KEY"],
        region_name="eu-central-003",
    )


def download_file(filename):
    s3 = get_b2_client()
    response = s3.get_object(Bucket=st.secrets["B2_BUCKET"], Key=filename)
    return response["Body"].read()


def file_exists(filename):
    s3 = get_b2_client()
    try:
        s3.head_object(Bucket=st.secrets["B2_BUCKET"], Key=filename)
        return True
    except:
        return False


# --- Helper to check file metadata ---
def get_file_version_token(filename):
    """Returns a unique token (ETag or LastModified) representing the file state."""
    s3 = get_b2_client()
    try:
        response = s3.head_object(Bucket=st.secrets["B2_BUCKET"], Key=filename)

        # Combine ETag and LastModified to create a robust version string
        return f"{response.get('ETag', '')}-{response.get('LastModified', '')}"
    except:
        return None


# --- Cached Data Fetcher ---
@st.cache_data(show_spinner="Lade Daten aus Cloud...")
def load_json_cached(filename, version_token):
    """
    This function actually downloads the file. Because it takes 'version_token'
    as an argument, Streamlit will hit the cache unless the version_token changes.
    """
    try:
        return json.loads(download_file(filename).decode("utf-8"))
    except (json.JSONDecodeError, Exception):
        return []
