#import things space
    #scrape
import asyncio 
from crawl4ai import AsyncWebCrawler
    #app
import streamlit as st

#APP UI
st.title("WebVoice: Know what your customers are saying quickly")
st.markdown("Enter one or more URLs below (one per line):")
input_text = st.text_area("Amazon Product URLs", height=150)
if st.button("Scrape Reviews"):
    urls = [line.strip() for line in input_text.splitlines() if line.strip()]
    all_reviews = []

    with st.spinner("Scraping reviews..."):
        for url in urls:
            reviews = scrape_reviews(url)
            all_reviews.extend(reviews)
#SCRAPE ACTIVITIES 
async def main():
    #create an instance OF ASYNC WEB CRAWLER
    async with AsyncWebCrawler as crawler:
        #run the crawler on a URL 
        result = await crawler.arun(url="#make code here to be for input")
#really quick
