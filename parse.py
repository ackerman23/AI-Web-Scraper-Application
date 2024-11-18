from langchain_ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate

# Modify the prompt to enforce proper CSV structure
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **Return Format:** Return the data in the CSV format with proper column headers. "
    "   Each value must not include extra quotes, and each row should be separated by a newline character. "
    "3. **CSV Structure:** Ensure the first line is the column headers, followed by the corresponding data rows."
    "   For example, if you're extracting Name, Academic Title, Email, and Personal Homepage, your output should look like this:\n"
    "   Name,Academic Title,Email,Personal Homepage\n"
    "   Chen Qun,Professor,chenbenben@nwpu.edu.cn,http://teacher.nwpu.edu.cn/en/1987000016.html\n"
    "   Li Zhanhuai,Professor,lizhh@nwpu.edu.cn,http://teacher.nwpu.edu.cn/en/lizhanhuai.html\n"
    "4. **No Extra Data:** Only include the data explicitly requested and nothing else."
)


llm = Ollama(model="llama2:3.2")

def parse_with_ollama(dom_chunks, parse_description, export_format):
    # Adjust the template based on the export format
    if export_format == "CSV":
        prompt = ChatPromptTemplate.from_template(template + "\nFormat: CSV")
    elif export_format == "JSON":
        prompt = ChatPromptTemplate.from_template(template + "\nFormat: JSON")
        
    chain = prompt | llm
    
    parsed_results = []
    
    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description})
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)
        
    return "\n".join(parsed_results)
