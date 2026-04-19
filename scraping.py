import wikipediaapi
import wikipedia
import os

def is_mental_health_related(title):
    keywords = [
        "mental", "depression", "anxiety", "stress",
        "disorder", "psychology", "psychiatry",
        "bipolar", "trauma", "therapy", "suicide",
        "phobia", "ocd", "addiction", "wellbeing"
    ]
    t = title.lower()
    return any(k in t for k in keywords)


def get_mental_health_data():
    wiki = wikipediaapi.Wikipedia(
        user_agent="Menahil Ikram_Bot/1.0 (menahilikram@gmail.com)",
        language="en",
    )

    os.makedirs("mental_health_data", exist_ok=True)

    # 🔥 powerful search queries
    queries = [
        "mental health",
        "mental disorders",
        "psychological disorders",
        "anxiety disorders",
        "depression disorders",
        "psychiatric conditions",
        "therapy types",
        "mental illness list",
        "phobias list",
        "stress disorders",
        "addiction disorders"
    ]

    all_titles = set()

    # 🔍 collect titles
    for q in queries:
        try:
            results = wikipedia.search(q, results=50)
            for r in results:
                if is_mental_health_related(r):
                    all_titles.add(r)
        except:
            pass

    print("Total collected titles:", len(all_titles))

    count = 0

    for title in all_titles:
        try:
            page = wiki.page(title)

            if page.exists() and len(page.text) > 1000:
                filename = title.replace(" ", "_").replace("/", "_")

                with open(f"mental_health_data/{filename}.txt", "w", encoding="utf-8") as f:
                    f.write(page.text)

                print("Saved:", title)
                count += 1

        except:
            print("Skipped:", title)

    print(f"\nDone! {count} files saved ✅")


if __name__ == "__main__":
    get_mental_health_data()