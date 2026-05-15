class Solution {
    public int lengthOfLongestSubstring(String s) {
         if (s.length() <= 1)
            return s.length();
        int res = 0;
        Map<Character, Integer> charIndex = new HashMap<>();
        int r = 0;
        while (r < s.length()) {
            if (charIndex.containsKey(s.charAt(r))) {
                res = Math.max(res, charIndex.size());
                r = charIndex.get(s.charAt(r)) + 1;
                charIndex.clear();
            }
            charIndex.put(s.charAt(r), r);
            r++;
        }
        res = Math.max(res, charIndex.size());
        return res;
    }
}
