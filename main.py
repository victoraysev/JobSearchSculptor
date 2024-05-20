import streamlit as st

from gui.result_tab import result_tab
from gui.setup_tab import setup_tab
from gui.scraper_tab import scraper_tab
from utils import scraper


def main():

    if st.session_state.get("setup_tab") == None:
        st.session_state["setup_tab"] = True
    if st.session_state.get("setup_tab"):
        setup_tab()
    elif st.session_state.get("scraper"):
        with st.spinner("Scraping..."):
            data = scraper.scrape(st.session_state["search_term"],
                                  st.session_state["results_wanted"],
                                  st.session_state["hours_old"],
                                  st.session_state["offset"])
        st.session_state["data"] = data
        st.session_state["scraper"] = False
        st.session_state["scraper_tab"] = True
        st.rerun()
    elif st.session_state.get("scraper_tab"):
        scraper_tab()
    elif st.session_state.get("result_tab"):
        result_tab()
if __name__ == '__main__':
    main()
