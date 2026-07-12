class Solution(object):
    def suggestedProducts(self, products, searchWord):
        out=[]
        products.sort()
        prefix=""
        for i in range(len(searchWord)):
            row=[]
            prefix+=searchWord[i]
            for prod in products:
                if prod.startswith(prefix):
                    row.append(prod)
                if len(row)==3:
                    break
            out.append(row)
        return out