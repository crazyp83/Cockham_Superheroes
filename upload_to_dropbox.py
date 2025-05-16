import sys
import dropbox
from dropbox.sharing import SharedLinkSettings, RequestedVisibility

def upload_to_dropbox(file_path, access_token):
    dbx = dropbox.Dropbox(access_token)
    with open(file_path, 'rb') as f:
        dbx.files_upload(f.read(), '/Cockham Superheros.ipa', mute=True)
    
    link_settings = SharedLinkSettings(requested_visibility=RequestedVisibility.PUBLIC)
    link = dbx.sharing_create_shared_link_with_settings('/Cockham Superheros.ipa', settings=link_settings)
    download_link = link.url.replace('?dl=0', '?dl=1')
    print(download_link)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python upload_to_dropbox.py <file_path> <access_token>")
        sys.exit(1)
    file_path = sys.argv[1]
    access_token = sys.argv[2]
    upload_to_dropbox(file_path, access_token)