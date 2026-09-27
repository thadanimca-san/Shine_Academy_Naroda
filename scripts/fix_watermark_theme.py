import glob

files = glob.glob('/home/ubuntu/Shine_Academy_Naroda/lib/**/*pdf*service*.dart', recursive=True)

for file_path in files:
    with open(file_path, 'r') as f:
        content = f.read()
    
    # 1. Fix the `pw.Document` inline theme declaration in the 4 pdf_generator_service files
    if 'theme: pw.ThemeData.withFont(base: regularFont, bold: boldFont)' in content:
        content = content.replace(
            "final pdf = pw.Document(\n      theme: pw.ThemeData.withFont(base: regularFont, bold: boldFont),\n    );",
            "final theme = pw.ThemeData.withFont(base: regularFont, bold: boldFont);\n    final pdf = pw.Document(theme: theme);"
        )
    
    # 2. Inject `theme: theme` into the `PdfBrandingUtil.getPageTheme` call
    # The current call looks like: pageTheme: await PdfBrandingUtil.getPageTheme(PdfPageFormat.a4)
    # We want to change it to: pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme)
    content = content.replace(
        "pageTheme: await PdfBrandingUtil.getPageTheme(PdfPageFormat.a4),",
        "pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),"
    )

    with open(file_path, 'w') as f:
        f.write(content)

print(f"Fixed {len(files)} files.")
