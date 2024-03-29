class Solution {
public:
    int result = 0;

    int averageOfSubtree(TreeNode* root) {
        traverse(root);
        return result;
    }

private:
    pair<int, int> traverse(TreeNode* node) {
        if (node == nullptr) return {0, 0};
        
        pair<int, int> left = traverse(node->left);
        pair<int, int> right = traverse(node->right);
        
        int currSum = node->val + left.first + right.first;
        int currCount = 1 + left.second + right.second;
        
        if (currSum / currCount == node->val) result++;
        
        return {currSum, currCount};
    }
};
