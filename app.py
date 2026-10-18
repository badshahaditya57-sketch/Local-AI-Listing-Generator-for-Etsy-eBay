import streamlit as st
import requests
import json

# Local Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

st.title("🛍️ Local AI Listing Generator for Etsy/eBay")
st.write("Generate polished product descriptions locally without paying for API tokens.")

product_name = st.text_input("What are you selling?", placeholder="e.g., Hand-carved wooden coffee table")
features = st.text_area("Key features (comma separated)", placeholder="e.g., walnut wood, mid-century modern, locally sourced")
target_platform = st.selectbox("Platform", ["Etsy", "eBay"])

if st.button("Generate Listing"):
    if product_name and features:
        prompt = f"Write a catchy, SEO-optimized product listing for {target_platform} for a '{product_name}'. Key features include: {features}. Make it professional but engaging."
        
        payload = {
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
        
        with st.spinner("Generating locally..."):
            response = requests.post(OLLAMA_URL, json=payload)
            if response.status_code == 200:
                result = response.json()["response"]
                st.subheader("Your Listing:")
                st.write(result)
            else:
                st.error("Make sure Ollama is running in the background!")