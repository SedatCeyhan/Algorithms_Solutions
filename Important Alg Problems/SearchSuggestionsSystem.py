'''

Given an array of strings products and a string searchWord. We want to design a system that suggests
at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with the searchWord.
If there are more than three products with a common prefix return the three lexicographically minimums products.
Return list of lists of the suggested products after each character of searchWord is typed

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]

Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

'''

class Solution:
    def suggestedProducts(self, products, searchWord):
        sol = []
        products = sorted(products)
        for i in range(len(searchWord)):
            subSearch, num = [], 0
            search = searchWord[:i + 1]
            for p in products:
                if num == 3: break
                if search in p[:i+1]:
                    subSearch.append(p)
                    num += 1
            sol.append(subSearch)

        return sol

sol = Solution()
products = ["havana"]
searchWord = "tatiana"
print(sol.suggestedProducts(products, searchWord))