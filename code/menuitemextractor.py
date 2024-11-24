if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price: str) -> float:
    return float(price.replace("$", "").replace(",", ""))

def clean_scraped_text(scraped_text: str) -> list[str]:
    scraped_text_lines = scraped_text.split("\n")
    item = []
    for line in scraped_text_lines:
        if line == "NEW" or line == "NEW!" or line == "" or line in ["S", "V", "GS", "P"]:
            continue
        else:
            item.append(line)
    return item

def extract_menu_item(title: str, scraped_text: str) -> MenuItem:
    item = clean_scraped_text(scraped_text)
    cleaned_price = clean_price(item[1])
    if len(item) < 3:
        description = "no description available"
    else:
        description = item[2]
    return MenuItem(name = item[0], price = cleaned_price, category = title, description = description)

if __name__=='__main__':
    pass
