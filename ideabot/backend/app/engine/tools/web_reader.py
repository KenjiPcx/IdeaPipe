import logging
import os
from typing import List, Optional

from llama_index.core.tools import FunctionTool
from llama_index.readers.web import FireCrawlWebReader
from pydantic import BaseModel

logger = logging.getLogger("uvicorn")


class WebReaderResult(BaseModel):
    content: str
    url: str
    is_error: bool
    error_message: Optional[str] = None


class FireCrawlReader:
    def __init__(self, api_key: Optional[str] = None):
        if api_key is None:
            api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError(
                "FIRECRAWL_API_KEY is required to use web reader. Get it here: https://www.firecrawl.dev/"
            )

        self.api_key = api_key
        self.reader = None

    def _init_reader(self, mode: str = "scrape"):
        """
        Lazily initialize the reader.
        """
        logger.info(f"Initializing FireCrawl reader in {mode} mode")
        self.reader = FireCrawlWebReader(
            api_key=self.api_key,
            mode=mode
        )

    def read_webpage(
        self,
        url: str,
        mode: str = "scrape",
    ) -> WebReaderResult:
        """
        Read content from a webpage using FireCrawl.
        
        Parameters:
            url (str): The URL to read content from
            mode (str): Either 'scrape' for single page or 'crawl' for website crawling
            **kwargs: Additional parameters to pass to FireCrawl
        """
        try:
            if self.reader is None:
                self._init_reader(mode)

            if self.reader:
                logger.info(f"Reading webpage: {url}")
                documents = self.reader.load_data(url=url)
                
                # Combine all document texts
                content = "\n\n".join([doc.text for doc in documents])
                
                return WebReaderResult(
                    content=content,
                    url=url,
                    is_error=False
                )
            else:
                raise ValueError("Reader is not initialized.")
                
        except Exception as e:
            error_message = f"Error reading webpage: {str(e)}"
            logger.error(error_message)
            return WebReaderResult(
                content="",
                url=url,
                is_error=True,
                error_message=error_message
            )


def get_tools(**kwargs):
    return [FunctionTool.from_defaults(FireCrawlReader(**kwargs).read_webpage)]
