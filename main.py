from timer import start_session, stop_session, view_sessions

while True:
    print("\n===== SnippetTimer =====")
    print("1. Start Session")
    print("2. Stop Session")
    print("3. View Sessions")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Session name: ")
        start_session(name)

    elif choice == "2":
        stop_session()

    elif choice == "3":
        view_sessions()

    elif choice == "4":
        break

    else:
        print("Invalid choice")
