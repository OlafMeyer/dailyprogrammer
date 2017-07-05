(defun scrabble (rack word)
  (cond ((null word) t)
        ((member (first word) rack)
          (scrabble (remove (first word) rack :count 1) (rest word)))
        ((member '? rack)
          (scrabble (remove '? rack :count 1) (rest word)))
        (t nil)))