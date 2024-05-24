from markdown_pdf import MarkdownPdf, Section

# 创建MarkdownPdf实例
pdf = MarkdownPdf()

# 添加Markdown内容。这里直接使用字符串，也可以从文件中读取。
# 注意：Markdown内容中包含中文。
markdown_content = """
# 标题

这是一个包含中文的Markdown文档。

## 小标题

- 列表项1
- 列表项2

**粗体文本** 和 *斜体文本*。
"""

# 将Markdown内容添加到PDF中。这里使用Section类来包装Markdown内容。
pdf.add_section(Section(markdown_content))

# 设置PDF文档的元数据
pdf.meta["title"] = "Markdown转PDF示例"
pdf.meta["author"] = "作者名"

# 保存PDF文件。指定文件名和路径。
pdf.save("markdown_to_pdf_example.pdf")
