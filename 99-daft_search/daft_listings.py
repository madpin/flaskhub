import schemas
from daftlistings import Daft, SearchType, SortType


async def get_daft_search_result():

    daft = Daft()

    daft.set_location("Dublin City")
    daft.set_search_type(SearchType.RESIDENTIAL_RENT)
    daft.set_min_price(1000)
    daft.set_max_price(1800)
    daft.set_sort_type(SortType.PUBLISH_DATE_DESC)

    listings = daft.search()
    result_items = []
    for listing in listings:
        searchItem = schemas.SearchItem(
            url=listing.daft_link,
            title=listing.title,
            monthly_price=listing.monthly_price,
            latitude=listing.latitude,
            longitude=listing.longitude,
            bedrooms=listing.bedrooms,
            bathrooms=listing.bathrooms,
            publish_date=listing.publish_date,
            category=listing.category,
            featured_level=listing.featured_level,
            sections=listing.sections,
            source_code=listing.shortcode,
        )
        result_items.append(searchItem)

        result = schemas.SearchResult(
            items=result_items,
            results_count=daft._total_results,
            search_rules=daft._make_payload()
        )
    return result
