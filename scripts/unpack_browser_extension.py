import zipfile


def extract_crx_file(crx_file_path, output_base_dir):
    try:
        zip_contents = zipfile.ZipFile(crx_file_path, 'r')
        parts = str(crx_file_path).split('/')
        crx_file_name = parts[1:][0]
        print("the crx file extracted is", crx_file_name)
        zip_contents.extractall(output_base_dir + "/" + crx_file_name)
    except Exception as e:
        print(f"Failed to extract crx file : {e}")
    
crx_file_path = '../edge_extensions_packed/088c7920-25da-45c8-be2a-24ec3b85e4ec.crx'
output_base_dir = '../edge_extensions_unpacked'
extract_crx_file(crx_file_path, output_base_dir)