import re

__all__ = (
    'TITLE_PATTERN',
    'PRODUCTS_PATTEREN',
)

TITLE_PATTERN = re.compile(r'<meta property="og:title" content=\"(.+)\"')
PRODUCTS_PATTEREN = re.compile((r"href=\"(/promo\S+)\""))
