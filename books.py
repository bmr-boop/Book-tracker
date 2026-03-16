import os
import json

BOOKS_FILE = "books.json"

def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_books(books):
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=2)

def show_books(books, filter_status=None):
    filtered = [b for b in books if filter_status is None or b["status"] == filter_status]
    if not filtered:
        print("\n📚 No books found!\n")
    else:
        print("\n📚 Your Book List:")
        for i, book in enumerate(filtered, 1):
            rating = f" ⭐ {book['rating']}/5" if book.get("rating") else ""
            print(f"  {i}. [{book['status'].upper()}] {book['title']} by {book['author']}{rating}")
        print()

def main():
    books = load_books()
    print("📚 Welcome to Your Book Tracker!")

    while True:
        print("What would you like to do?")
        print("  1 - View all books")
        print("  2 - View by status")
        print("  3 - Add a book")
        print("  4 - Update book status")
        print("  5 - Rate a book")
        print("  6 - Delete a book")
        print("  7 - Quit")

        choice = input("\nEnter choice (1-7): ").strip()

        if choice == "1":
            show_books(books)

        elif choice == "2":
            print("  1 - Want to Read")
            print("  2 - Reading")
            print("  3 - Finished")
            s = input("Choose status: ").strip()
            statuses = {"1": "want to read", "2": "reading", "3": "finished"}
            if s in statuses:
                show_books(books, statuses[s])

        elif choice == "3":
            title = input("Book title: ").strip()
            author = input("Author: ").strip()
            print("  1 - Want to Read  2 - Reading  3 - Finished")
            s = input("Status: ").strip()
            statuses = {"1": "want to read", "2": "reading", "3": "finished"}
            status = statuses.get(s, "want to read")
            books.append({"title": title, "author": author, 
                         "status": status, "rating": None})
            save_books(books)
            print(f"✅ Added '{title}'!\n")

        elif choice == "4":
            show_books(books)
            try:
                num = int(input("Enter book number to update: "))
                if 1 <= num <= len(books):
                    print("  1 - Want to Read  2 - Reading  3 - Finished")
                    s = input("New status: ").strip()
                    statuses = {"1": "want to read", "2": "reading", "3": "finished"}
                    if s in statuses:
                        books[num-1]["status"] = statuses[s]
                        save_books(books)
                        print("✅ Status updated!\n")
            except ValueError:
                print("❌ Please enter a number.\n")

        elif choice == "5":
            show_books(books, "finished")
            try:
                num = int(input("Enter book number to rate: "))
                if 1 <= num <= len(books):
                    rating = int(input("Rating (1-5): "))
                    if 1 <= rating <= 5:
                        books[num-1]["rating"] = rating
                        save_books(books)
                        print(f"⭐ Rated {rating}/5!\n")
            except ValueError:
                print("❌ Please enter a number.\n")

        elif choice == "6":
            show_books(books)
            try:
                num = int(input("Enter book number to delete: "))
                if 1 <= num <= len(books):
                    deleted = books.pop(num-1)
                    save_books(books)
                    print(f"🗑️ Deleted '{deleted['title']}'\n")
            except ValueError:
                print("❌ Please enter a number.\n")

        elif choice == "7":
            print("👋 Happy reading!")
            break

        else:
            print("❌ Please enter 1–7.\n")

main()
