from typing import List, Dict
from collections import defaultdict


class Solution:
    def favoriteGenre(self, userMap: Dict[str, List],
                      genreMap: Dict[str, List]) -> Dict[str, List]:
        # users * average numbers songs = n*k + N (number of songs we have)

        # create a songs -> genre mapping
        songsToGenre = defaultdict(str)
        for genre in genreMap:  # N
            songs = genreMap[genre]
            for song in songs:
                songsToGenre[song] = genre

        res = defaultdict(list)

        # go over users and create count map
        for user in userMap.keys():  # m users * k songs listened to
            # res[user] = []
            countMap = defaultdict(int)
            maxG = -2**31
            songs = userMap[user]
            for song in songs:
                genre = songsToGenre[song]
                countMap[genre] += 1
                maxG = max(maxG, countMap[genre])

            # get all genres with max count
            for genre in countMap.keys():
                if countMap[genre] == maxG:
                    res[user].append(genre)

        return res


if __name__ == '__main__':
    userSongs = {
        "David": ["song1", "song2", "song3", "song4", "song8"],
        "Emma":  ["song5", "song6", "song7"]
    }

    songGenres = {
        "Rock":    ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno":  ["song2", "song4"],
        "Pop":     ["song5", "song6"],
        "Jazz":    ["song8", "song9"]
    }
    s = Solution()
    print(s.favoriteGenre(userSongs, songGenres))
