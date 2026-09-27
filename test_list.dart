void main() {
  List<int> unmod = List.unmodifiable([1, 2, 3]);
  try {
    unmod.insert(0, 0);
  } catch(e) {
    print(e);
  }
}
