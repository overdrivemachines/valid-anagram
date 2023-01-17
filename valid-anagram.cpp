#include <iostream>
#include <map>

using namespace std;

bool isAnagram(string s, string t) {
  map<char, int> letters;

  if (s.length() != t.length())
    return false;
  for (auto c: s) {
    letters[c]++;
  }

  for (auto c: t) {
    letters[c]--;
    if (letters[c] < 0)
      return false;
  }

  return true;
}

int main(int argc, char const *argv[]) {

  cout << isAnagram("anagram", "nagaram") << "\n";
  cout << isAnagram("rat", "car") << "\n";

  return 0;
}
