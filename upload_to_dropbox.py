import dropbox

# Initialize Dropbox client (replace with your access token)
dbx = dropbox.Dropbox("YOUR_ACCESS_TOKEN")

# Open the file to upload
with open("local_file.txt", "rb") as f:
    chunk_size = 4 * 1024 * 1024  # 4MB chunks
    
    # Start the upload session
    session_start_result = dbx.files_upload_session_start(f.read(chunk_size))
    cursor = dropbox.files.UploadSessionCursor(
        session_id=session_start_result.session_id,
        offset=f.tell()
    )
    
    # Append more data (if applicable)
    dbx.files_upload_session_append_v2(f.read(chunk_size), cursor)
    
    # Finish the upload
    commit = dropbox.files.CommitInfo(path="/remote_file.txt")
    dbx.files_upload_session_finish(f.read(chunk_size), cursor, commit)