import sys,os
sys.path.append(f'{os.getcwd()[:-11]}')
def test_all():
  os.system("python3 basics_test.py")
  os.system("python3 graph_test.py")
  os.system("python3 search_test.py")
  os.system("python3 TestBin2Hex.py")
  os.system("python3 TestFibRefactored.py")
  print("all test succeed...")
  return "ok"
  
#test all methods  
test_all()

