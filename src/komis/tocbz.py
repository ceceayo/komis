from pathlib import Path

from cbz.comic import ComicInfo
from cbz.constants import AgeRating, Format, Manga, PageType, YesNo
from cbz.page import PageInfo


def comic_to_cbz(dir_name: str, out_file: str):
    """Turn a comic into a cbz archive."""
    pages = list(Path(dir_name).iterdir())
    print(pages)
    comic_pages = []
    for i in range(len(pages)):
        if pages[i].name.split(".")[0] == "full":
            continue
        comic_pages.append(PageInfo.load(path=pages[i].absolute(), type=PageType.STORY))
    comic = ComicInfo.from_pages(
        pages=comic_pages,
        title="Your Comic Title",
        series="Your Comic Series",
        number=1,
        language_iso="en",
        format=Format.WEB_COMIC,
        black_white=YesNo.NO,
        manga=Manga.NO,
        age_rating=AgeRating.PENDING,
    )

    cbz_content = comic.pack()
    Path(out_file).write_bytes(cbz_content)
