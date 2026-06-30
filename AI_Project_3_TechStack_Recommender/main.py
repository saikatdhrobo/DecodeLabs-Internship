from recommender import TechStackRecommender


def onboarding():

    print("=" * 50)
    print("Welcome to AI Tech Stack Recommender")
    print("=" * 50)

    name = input("Enter your name: ")

    print(f"\nHello {name}!")

    print("\nPlease answer a few questions.")

    print("\nEnter at least THREE skills/interests.")

    skills = []

    while len(skills) < 3:

        skill = input(f"Skill {len(skills)+1}: ").strip()

        if skill != "":
            skills.append(skill)

    return name, skills


def main():

    name, skills = onboarding()

    recommender = TechStackRecommender(
        "dataset/raw_skills.csv"
    )

    results = recommender.recommend(
        skills,
        top_n=3
    )

    print("\n")
    print("=" * 60)
    print(f"Top Career Recommendations for {name}")
    print("=" * 60)

    for i, row in enumerate(results.itertuples(), start=1):

        print(f"\n{i}. {row.Career}")

        print(f"Similarity Score : {row.Score:.3f}")

        print(f"Required Skills  : {row.Skills}")

    print("\nThank you for using the recommender!")


if __name__ == "__main__":
    main()