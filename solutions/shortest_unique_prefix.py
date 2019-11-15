class Node:
    def __init__(self):
        self.count = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = Node()
            current = current.children[c]
            current.count += 1

    def get_prefix(self, word):
        result = ""
        current = self.root
        for c in word:
            if current.count == 1:
                return result
            result += c
            current = current.children[c]
        return result


def get_prefixes_2(words):
    result = []
    for index, word in enumerate(words):
        current = ""
        for c in word:
            current += c
            if current not in [w[:len(current)] for w in  words[:index]+words[index+1:]]:
                result.append(current)
                break
    print(result)
    return result


def get_prefixes(words):
    results = []
    trie = Trie()

    for word in words:
        trie.insert(word)
    for word in words:
        results.append(trie.get_prefix(word))
    return results


def main():
    assert get_prefixes(['joma', 'john', 'jack', 'techlead']) == ['jom', 'joh', 'ja', 't']
    assert get_prefixes_2(['joma', 'john', 'jack', 'techlead']) == ['jom', 'joh', 'ja', 't']


if __name__ == '__main__':
    main()
