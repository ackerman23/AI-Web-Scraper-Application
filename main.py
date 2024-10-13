import streamlit as st
from scrape import scrape_website, split_dom_content, extract_body_content, clean_body_content
from parse import parse_with_ollama
import pandas as pd
import json

st.title("Professors info Scraper")
url = st.text_input("Enter a Website URL: ")

# Add an option to choose the output format
export_format = st.selectbox("Choose export format:", ["CSV", "JSON", "Database"])

if st.button("Scrape Site"):
    st.write("Scraping the website")
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content
    
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")
    
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")
            
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_results = parse_with_ollama(dom_chunks, parse_description,export_format)
            st.write(parsed_results)
            
            # Save the parsed results based on the selected export format
            if export_format == "CSV":
                # Convert to DataFrame and save as CSV
                df = pd.DataFrame({"Parsed Results": parsed_results.split('\n')})
                csv = df.to_csv(index=False)
                
                # Provide a download button for CSV
                st.download_button("Download CSV", csv, "parsed_results.csv", "text/csv")
                
            elif export_format == "JSON":
                # Convert to JSON
                json_data = json.dumps({"Parsed Results": parsed_results.split('\n')}, indent=4)
                
                # Provide a download button for JSON
                st.download_button("Download JSON", json_data, "parsed_results.json", "application/json")
                
            elif export_format == "Database":
                st.write("Saving to database (coming soon)...")  # Add database logic later

