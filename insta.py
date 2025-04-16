import json

# Load JSON data
with open('followers_1.json', 'r', encoding='utf-8') as f:
    followers_data = json.load(f)

with open('following.json', 'r', encoding='utf-8') as f:
    following_data = json.load(f)

# Extract usernames
followers = {entry['string_list_data'][0]['value'] for entry in followers_data}
following = {entry['string_list_data'][0]['value'] for entry in following_data['relationships_following']}

# Find non-followers
not_following_back = sorted(following - followers)

# Print results
print(f"You're following {len(following)} people.")
print(f"You have {len(followers)} followers.")
print(f"\nPeople who don't follow you back ({len(not_following_back)}):\n")

for user in not_following_back:
    print(f"- {user}")

# Write to file
with open('not_following_back.txt', 'w', encoding='utf-8') as f:
    f.write("People you follow who don't follow you back:\n")
    for user in not_following_back:
        f.write(f"{user}\n")

print("\n📄 Results saved to not_following_back.txt")
