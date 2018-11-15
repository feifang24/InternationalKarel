from lxml import html
from google.cloud import translate
from translate_code import translate_code
import os
import sys

translate_client = translate.Client()

all_languages = [lng['language'] for lng in translate_client.get_languages()]

def translate_text(text, target_language):
	return translate_client.translate(text, target_language=target_language)['translatedText']

def separate_code_from_file(filename):
    with open(filename, "r") as f:
        page = f.read()
    tree = html.fromstring(page)
    code_list = tree.xpath('//code/text()')
    
    for code in code_list:
        page = page.replace(code, '',1)

    return [page, code_list]

def translate_file(page, code_list, target_language):
	import pdb;pdb.set_trace()

	translated_page = translate_text(page, target_language)

	for code in code_list:
		translated_code = translate_code(code, target_language)
		translated_page = translated_page.replace("<code></code>", "<code>" + translated_code + "</code>", 1) 

	return translated_page

def output_translation(translated_page, filename):
	Html_file= open(filename,"w")
	Html_file.write(translated_page)
	Html_file.close()

def translate_output_file(filename, target_languages=all_languages):
	#import pdb;pdb.set_trace();
	filename_raw = filename.split(".")[0].split("/")[-1]
	output_dir = filename.split(".")[0][:-len(filename_raw)] + "/output/"
	file_output_dir = output_dir + filename_raw + "/"
	if not os.path.isdir(file_output_dir):
		os.mkdir(file_output_dir)

	page, code_list = separate_code_from_file(filename)

	for language in target_languages:
		translated_file = translate_file(page, code_list, language)
		output_filename = file_output_dir + filename_raw + '-' + language + '.html'
		output_translation(translated_file, output_filename)

def main():
	filename = sys.argv[1]
	target_languages = all_languages
	if len(sys.argv) > 2:
		target_languages = [sys.argv[i] for i in range(2,len(sys.argv))]	
	translate_output_file(filename, target_languages=target_languages)

if __name__ == "__main__":
    main()
