import os

def deduplicate_files_in_directory():
  """
  Remove files that are copies in the current folder
  """
  # 1. find all files in the folder
  # 2. delete the ones that have “copy” in the name
  files_in_current_directory = os.listdir('.')
 
  for filename in files_in_current_directory:
    if "copy" in filename:
      os.remove('./' + filename)

# deduplicate_files_in_directory()



# 1. create some files
# 2. copy a subset of those files
# 3. run `deduplicate_files_in_directory`
# 4. check if the result is what we expect
# 5. clean up the files we created
def test_deduplicate_files_in_directory():
  # create some files
  for i in range(10):
    open('./file-{0}.txt'.format(i), 'w').close()

    # make copy of same file for "even" files
    is_even_number = i % 2 == 0
    if is_even_number:
      open('./file-{0} copy.txt'.format(i), 'w').close()

  # call the function we want to test
  deduplicate_files_in_directory()

  # check if the result is what we expect
  has_failures = False
  files_in_current_directory = os.listdir('.')
  for filename in files_in_current_directory:
    if "copy" in filename:
      has_failures = True

  if has_failures:
    print("FAIL: there are copies in the directory")
  else:
    print("PASS!")

  # clean up the files we created
  # IMPORTANT: this assumes anything with "file-" is a created file, 
  #            and will delete it
  for filename in files_in_current_directory:
    if 'file-' in filename:
      os.remove(filename)



  
  
test_deduplicate_files_in_directory()