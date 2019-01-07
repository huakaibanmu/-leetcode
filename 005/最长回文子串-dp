class LongestPalindrome {
  	boolean result[][];//存储dp信息，result[i][j]存储的是s[i],...s[j]是否是回文子串
	int left = 0;
	int right = 0;
	int MAX = -1;
	String maxstring = "";

	public String longestPalindrome(String s) {
		int n = s.length();
		result = new boolean[n][n];
		if (s.equals(""))
			return "";
		for (int i = 0; i < n; i++) {
			result[i][i] = true;
			if (i == n - 1)
				break;
			result[i][i + 1] = (s.charAt(i) == s.charAt(i + 1));

		}
		for (int i = n - 2; i >= 0; i--) {//求状态数组，通过判断子串是否回文判断当前串是否回文，因此i倒序遍历，j正序遍历
			for (int j = 1; j < n; j++) {
				if (result[i + 1][j - 1] == true && s.charAt(i) == s.charAt(j)) {
					result[i][j] = true;
				}

			}

		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (result[i][j] && j - i > MAX) {
					MAX = j - i;
					maxstring = s.substring(i, j + 1);
				}

			}
		}
		return maxstring;

	}
}
