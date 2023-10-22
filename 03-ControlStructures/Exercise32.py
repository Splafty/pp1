interested_in_computer_science = False
like_playing_computer_games = False
has_instagram_account = False

interested_in_computer_science = input("Are you interested in computer science? (Y/N): ").strip().upper() == "Y"
like_playing_computer_games = input("Do you like playing computer games? (Y/N): ").strip().upper() == "Y"
has_instagram_account = input("Do you have an Instagram account? (Y/N): ").strip().upper() == "Y"

print("Interested in computer science: " + ("Yes" if interested_in_computer_science else "No"))
print("Playing computer games: " + ("Yes" if like_playing_computer_games else "No"))
print("Has an Instagram account: " + ("Yes" if has_instagram_account else "No"))
