from pypdf import PdfWriter
from pyhanko.sign import signers
from pyhanko.pdf_utils.writer import copy_into_new_writer
from pyhanko.pdf_utils.reader import PdfFileReader
from cryptography.hazmat.primitives.serialization import pkcs12

def merge_and_sign_files(file_paths, output_path):
    writer = PdfWriter()
    for pdf_path in file_paths:
        writer.append(pdf_path)
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)

    with open(output_path, 'rb+') as merged_file:
        reader = PdfFileReader(merged_file)
        writer = copy_into_new_writer(reader)

        # Update this with your actual pfx path
        pfx_path = './certificate.pfx'
        # Update this with your actual pfx password (as bytes)
        pfx_password = b'password'

        with open(pfx_path, 'rb') as pfx_file:
            pfx_data = pfx_file.read()

        private_key, certificate, additional_certificates = pkcs12.load_key_and_certificates(pfx_data, pfx_password)

        signer = signers.SimpleSigner(
            signing_key=private_key,
            signing_cert=certificate,
            cert_registry=additional_certificates
        )

        signers.sign_pdf(
            writer,
            signers.PdfSignatureMetadata(
                field_name='MergedDocumentSignature',
                reason='Validating merged document',
                contact_info='Your contact info',
                subfilter=signers.constants.DEFAULT_SIG_SUBFILTER
            ),
            signer=signer
        )

if __name__ == "__main__":
    file_paths = [
        "./Signed.pdf",
        "./Signed.pdf"
    ]
    output_file = "./Combined.pdf"

    merge_and_sign_files(file_paths, output_file)
