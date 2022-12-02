(defparameter *input-file* "../puzzles/day-01.input")

(defun get-input-lines (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
          while line
          collect line)))

(defun get-calories (filename)
  (map 'list #'(lambda (s)
                 (parse-integer s :junk-allowed t))
       (get-input-lines filename)))


(defun partition-data (lst)
  (loop with part
        for el in lst
        if (equal el nil)
          collect (nreverse part) into result and do (setf part nil)
        else
          do (push el part)
        finally (return (nconc result (list (nreverse part))))))

(defun sum-partitions (lst)
  (map 'list #'(lambda (sublist)
                 (reduce #'+ sublist))
       lst))


(defun solve-part-1 (calories)
  (let ((calorie-groups (partition-data calories)))
      (apply #'max (sum-partitions calorie-groups))))

(defun solve-part-2 (calories)
  (let ((calorie-groups (partition-data calories)))
    (reduce #'+ (subseq (sort (sum-partitions calorie-groups) #'>) 0 3))))

(defun solve ()
  (let ((calories (get-calories *input-file*)))
    (fresh-line)
    (princ "Part 1: ")
    (princ (solve-part-1 calories))
    (fresh-line)
    (princ "Part 2: ")
    (princ (solve-part-2 calories))))
