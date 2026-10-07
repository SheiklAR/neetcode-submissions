class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {} # child email: parent email
        rank = defaultdict(lambda : 1)
        name = {}

        def find(vertex):
            if parent[vertex] == vertex:
                return vertex
            
            parent[vertex] = find(parent[vertex])
            return parent[vertex]


        def union(email1, email2):
            parent_1 = find(email1)
            parent_2 = find(email2)

            if parent_1 == parent_2:
                return parent_1
            
            if rank[parent_1] >= rank[parent_2]:
                rank[parent_1] += rank[parent_2] 
                parent[parent_2] = parent_1
                return parent_1
            else:
                rank[parent_2] += rank[parent_1] 
                parent[parent_1] = parent_2
                return parent_2



        
        
        # union
        for account in accounts:
            first_email = account[1]
            curr_parent = first_email
            if first_email in parent:
                rank[first_email] += 1
                curr_parent = find(first_email)
            # first email is the parent
            parent[first_email] = curr_parent
            name[first_email] = account[0]
            # print(name)

            for email in account[2:]:
                print('in')
                # from second we do union:
                if email in parent:
                    curr_parent = union(curr_parent, email)
                
                parent[email] = curr_parent
        


        group = defaultdict(set)


        for child_email, father_email in parent.items():
            print('here')
            group[find(father_email)].add(child_email)
        
        print(group)
        ans = []

        for key,val in group.items():
            ans.append([name[key]] + sorted(list(val)))
        
        return ans