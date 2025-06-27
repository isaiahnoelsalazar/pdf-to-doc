def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS_1

def convert_to_pdf(input_pdf_path, output_docx_path):
    try:
        pdf_file = input_pdf_path
        docx_file = output_docx_path

        cv = Converter(pdf_file)
        cv.convert(docx_file)
        cv.close()
        return True
    except:
        return False


result = None

if "file" not in request.files:
    result = redirect(request.url)

file = request.files["file"]

if file.filename == "":
    result = redirect(request.url)

if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    # unique_filename = str(uuid.uuid4()) + "_" + filename
    pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(pdf_path)

    pdf_filename = os.path.splitext(filename)[0] + ".docx"
    doc_path = os.path.join(app.config["CONVERTED_FOLDER_1"], pdf_filename)

    if convert_to_pdf(pdf_path, doc_path):
        result = send_file("/home/sasasaia/" + app.config["CONVERTED_FOLDER_1"] + "/" + pdf_filename, as_attachment=True, download_name=pdf_filename)
        os.remove(pdf_path)
        os.remove("/home/sasasaia/" + app.config["CONVERTED_FOLDER_1"] + "/" + pdf_filename)
    else:
        result = "<h1>Error: PDF to DOC conversion failed.</h1><p>Please check server logs for more details.</p>"
else:
    result = "<h1>Error: Invalid file type. Only *.pdf files are allowed.</h1>"

