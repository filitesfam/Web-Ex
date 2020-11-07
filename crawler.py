import requests
from bs4 import BeautifulSoup
from Database import Database

def get_soup(url):
    page = requests.get(url)
    contents = page.content
    soup = BeautifulSoup(contents, "html.parser")
    return soup


def get_doctors_page_url(content):
    doctors_pages_url = []
    for a in content.find_all('a', {"class": "provider-link"}):
        doctors_pages_url.append(a["href"])
    return doctors_pages_url


def process_doctor_info(doctor_page_url: list):
    doctor_info = []
    for i in range(1, len(doctor_page_url)):
        doctor_page_content = get_soup("https://www.caredash.com" + doctor_page_url[i])
        doctor_address = get_doctor_address(doctor_page_content)
        doctor_info.append({
            "name": get_doctor_name(doctor_page_content).replace('\n', ''),
            "rate": get_doctor_rate(doctor_page_content),
            "city": doctor_address[1].replace(',', ''),
            "address": doctor_address[0].replace('\n', ''),
            "page": doctor_page_url[i],
            "specialty": get_doctor_specialty(doctor_page_content),
            "rate_detail": get_doctor_overall_rate(doctor_page_content),
            "reviews": get_review(doctor_page_content)
        })
    database = Database()
    database.insert_info(doctor_info)


def get_doctor_name(doctor_page_content):
    return doctor_page_content.find("h1", {"class": "cd1-name"}).text


def get_doctor_rate(doctor_page_content: BeautifulSoup):
    try:
        profile_section = doctor_page_content.find("div", {"class": "force-profile-flip"}).find("span", {"class": "num-ratings"}).text

        return float(profile_section)
    except ValueError:
        return "null"


def get_doctor_address(doctor_page_content: BeautifulSoup):
    doctor_address = []
    doctor_address.append(doctor_page_content.find("div", {"class": "p-content"}).find("p").text.replace("\n", ""))
    doctor_address.append(doctor_page_content.find("div", {"class": "p-content"}).find("span").text.replace("\n", ""))
    return doctor_address


def get_doctor_specialty(doctor_page_content: BeautifulSoup):
    specialty = []
    specialty_tag = doctor_page_content.find("div", {"id": "specialties_section"})
    specialty_tag_a = doctor_page_content.find("div", {"id": "specialties_section"}).find_all("a")
    if not specialty_tag_a:
        specialty.append(specialty_tag.find("span", {"class": "font-weight-normal"}).text.replace("\n", ""))
    else:
        for a in specialty_tag_a:
            specialty.append(a.text.replace("\n", ""))
    return specialty


def get_doctor_overall_rate(doctor_page_content: BeautifulSoup):
    review_subjects = ["Communication", "Scheduling", "Staff", "Treatment", "Bedside Manner", "Average Wait Time"]

    overall_rate = {}
    overall_rating_item = doctor_page_content.find("div", {"class": "review-item-container"})

    if overall_rating_item is None:
        return None
    else:
        overall_rating_item = overall_rating_item.find("div", {"class": "average-ratings"})
        if overall_rating_item is not None:
            overall_rating_item = overall_rating_item.find_all("div", {"class": "rating-item"})
            for rating in overall_rating_item:
                rate_subject = rating.find("div", {"class": "set-xs-width"})
                rate_amount = rating.find("span", {"class": "num-ratings"})
                if rate_subject and rate_amount is not None:
                    overall_rate[rate_subject.find("h6").text.replace("\n", "").replace(":", "")] = rate_amount.find("strong").text
                    review_subjects.remove(rate_subject.find("h6").text.replace("\n", "").replace(":", ""))
                elif rate_amount is None and rate_subject is not None:
                    overall_rate[rate_subject.find("h6").text.replace("\n", "").replace(":", "")] = rate_subject.find("div", {"class": "p-content"}).text.replace("\n\n", "")
                    review_subjects.remove(rate_subject.find("h6").text.replace("\n", "").replace(":", ""))
            for review_subject in review_subjects:
                overall_rate[review_subject] = "null"

    return overall_rate


def get_review(doctor_page_content: BeautifulSoup):
    reviews = []
    review_tag = doctor_page_content.find("div", {"id": "provider_reviews"})
    if review_tag is not None:
        review_container = review_tag.find_all("div", {"class": "review-item-container"})
        for review in review_container:
            review_details = get_detail_review(review)
            title = review.find("div", {"class": "review-item-title"})
            if title is not None:
                title = title.text.replace("\n", "")
            content = review.find("div", {"class": "review-body-text"}).find("p").text.replace("\n", "")
            reviewer_name = review.find("div", {"class": "review-item-name"}).find("strong").text.replace("\n", "")
            reviewer_status = review.find("div", {"class": "reviewer-status"})
            if reviewer_status is not None:
                reviewer_status = reviewer_status.text.replace("\n", "")
            reviews.append({
                "title": title,
                "content": content,
                "reviewer_name": reviewer_name,
                "reviewer_status": reviewer_status,
                "review_details": review_details
            })
    return reviews


def get_detail_review(review: BeautifulSoup):
    review_detail = {}
    review_subjects = ["Communication", "Scheduling", "Staff", "Treatment", "Bedside Manner"]
    detail = review.find("div", {"class": "profile-user-reviews"})
    if detail is not None:
        rating_items = detail.find_all("div", {"class": "col-6 rating-item margin-bottom"})
        for rating_item in rating_items:
            review_detail[rating_item.find("h6").text.replace(":", "").replace("\n", "")] = len(rating_item.find_all("span", {"class": "icon-star-full doctor-rating"}))
            review_subjects.remove(rating_item.find("h6").text.replace(":", "").replace("\n", ""))
        waiting_time = detail.find("div", {"class": "col-6 rating-item wait-time"})
        if waiting_time is not None:
            review_detail["Wait Time"] = waiting_time.find("p", {"class": "small"}).text.replace("\n", "")
        else:
            review_detail["Wait Time"] = "null"
        for review_subject in review_subjects:
            review_detail[review_subject] = "null"
    if not review_detail:
        return None
    else:
        return review_detail


def plot_doctor_rate_based_on_specialty():
    database = Database()
    database.calculate_doctor_rate_based_on_specialty()


def plot_doctor_overall_rate():
    database = Database()
    database.calculate_number_of_doctor_overall_rate()

def main():
    # it will run the crawler
    # for i in range(99, 101):
    #     print(i)
    #     content = get_soup("https://www.caredash.com/csearch?utf8=%E2%9C%93&autocomplete_type=&q=&loc=Chicago%2C+IL%2C+USA&pt=41.878114%2C-87.629798&state=IL&page=" + str(i))
    #     doctor_urls = get_doctors_page_url(content)
    #     print(process_doctor_info(doctor_urls))
    #     doctor_urls.clear()

    # plot_doctor_rate_based_on_specialty()
    plot_doctor_overall_rate()




if __name__ == "__main__":
    main()
