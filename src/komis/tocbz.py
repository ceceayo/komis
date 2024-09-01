from pathlib import Path
from tempfile import TemporaryDirectory

from cbz.comic import ComicInfo
from cbz.constants import AgeRating, Format, Manga, PageType, YesNo
from cbz.page import PageInfo

from komis.main import create_the_comic


def comic_to_cbz(
    komis_file: str,
    out_file: str,
    comic_title: str = "TITLE",
    series_title: str = "SERIES",
    issue: int = 0,
    lang: str = "en",
):
    """Turn a comic into a cbz archive."""
    _, _, _, images = create_the_comic(komis_file)
    pages = []
    with TemporaryDirectory() as wdir:
        for im in range(len(images)):
            images[im].save(wdir + f"/{im}.jpg")
            pages.append(
                PageInfo.load(
                    path=wdir + f"/{im}.jpg",
                    type=PageType.FRONT_COVER if im == 0 else PageType.STORY,
                )
            )
        comic = ComicInfo.from_pages(
            pages=pages,
            title=comic_title,
            series=series_title,
            number=issue,
            language_iso=lang,
            format=Format.WEB_COMIC,
            black_white=YesNo.NO,
            manga=Manga.NO,
            age_rating=AgeRating.PENDING,
        )

        cbz_content = comic.pack()
    Path(out_file).write_bytes(cbz_content)
