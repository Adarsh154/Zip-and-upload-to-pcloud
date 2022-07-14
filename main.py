from pcloud import PyCloud
import shutil
import datetime


def make_zip():
    # Function used to amke zip file which will be further uploaded to pcloud
    # Replace following with your directory, filenames
    directory = 'G:\\Tally ERP 9.6\\data1'

    file_name = 'Tally_backup_' + str(datetime.date.today().strftime("%d-%m-%y"))

    shutil.make_archive(file_name, 'zip', directory)
    return file_name


def pcloud_connect():
    """Create a connection to Pcloud."""
    pc = None
    try:
        pc = PyCloud('Your_username', 'Your_password')
        print("Login Successful")
    except Exception as e:
        print('Error connecting to Pcloud: ' + str(e))
    return pc


def pcloud_upload_file(local_file, pcloud_file_path):
    try:
        pc = pcloud_connect()
        pc.uploadfile(files=[local_file], path=pcloud_file_path)
        print("Upload Successful")
    except Exception as e:
        print('Error uploading file to pcloud: ' + str(e))


backup_file_name = make_zip() + '.zip'
# backup_file_name = 'Tally_backup_14-07-22' + '.zip'
pcloud_upload_file(backup_file_name, '/Tally_data')
