class Solution:
    encode_code="#encoded#"
    def encode(self, strs: List[str]) -> str:
        if len(strs)==0: return "#encoded#empty#"
        return self.encode_code.join(strs)

    def decode(self, s: str) -> List[str]:
        if s=="#encoded#empty#": return []
        return s.split(self.encode_code)
