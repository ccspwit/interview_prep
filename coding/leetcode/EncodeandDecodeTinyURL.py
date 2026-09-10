# -*- coding: utf-8 -*-
"""
Created on June 15, 2019
LeetCode problem 535
TinyURL is a URL shortening service where you enter a URL such
as https://leetcode.com/problems/design-tinyurl and it returns
a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm
should work. You just need to ensure that a URL can be encoded
to a tiny URL and the tiny URL can be decoded to the original
URL
@author: K Li
"""
class Codec:
    def __init__(self):
        self.store = {}
        self.counter = 0
        self.mapping = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.size = len(self.mapping)

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        # convert count to 62-alphebet string, reverse order
        self.store[self.counter] = longUrl
        surl = []
        c = self.counter
        if c == 0:
            surl = [self.mapping[0]]
        else:
            while c > 0:
                c, rem = divmod(c, self.size)
                surl.append(self.mapping[rem])
        self.counter += 1
        return ''.join(surl)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        # convert reverse order short url to number
        counter = 0
        for ch in shortUrl:
            counter = counter*self.size + self.mapping.index(ch)

        return self.store[counter]   

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))