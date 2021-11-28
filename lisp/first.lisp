#!/usr/local/bin/sbcl --script

  #-quicklisp
  (let ((quicklisp-init (merge-pathnames ".quicklisp/setup.lisp"
                                         (user-homedir-pathname))))
    (when (probe-file quicklisp-init)
      (load quicklisp-init)))

(ql:quickload :cl-csv)
(use-package :iterate)
(ql:quickload :parse-float)
(use-package :parse-float)

(defvar datacsv (cl-csv:read-csv #P"./dano.csv"))

(print datacsv)

(defun parse-string-to-floats (line)
  (loop
    :with n := (length line)
    :for pos := 0 :then chars
    :while (< pos n)
    :for (float chars) := (multiple-value-list
            (read-from-string line nil nil :start pos))
    :collect float))

(defun firstSecondElement (it)
  (parse-integer (car it))
)

(defun lastElement (it)
	(parse-float (cadr it))
)

(defun secondElement (it)
        (parse-integer (caddr it))
)

(defvar workDataTaskOne
  (map 'list (lambda (it) (firstSecondElement it)) (cdr datacsv))
)

(defvar workDataTwo
	(map 'list (lambda (it) (lastElement it)) (cdr datacsv))
)


(defvar workDataThree
        (map 'list (lambda (it) (secondElement it)) (cdr datacsv))
)


(print workDataTaskOne)
(print workDataTwo)
(print workDataThree)

(defun multiply(a b)
  (if (eq a nil)
      0
    (+
      (* (car a) (car b))
      (multiply (cdr a) (cdr b)))))

(defvar ans (multiply workDataTaskOne workDataTwo))

(print ans)


(defun square (x)  
  (* x x)) 

(defun multiplyTwo(a b)
  (if (eq a nil)
      0
    (+
      (* (car a) (car b))
      (multiplyTwo (cdr a) (cdr b)))))


(defvar ansTwo (multiplyTwo workDataTaskOne workDataThree))

(print ansTwo)


(defun disp (a b)
(if (eq a nil)
	0     
     (+
       (square(- (car a) b))
      (disp (cdr a) b)))
)
(defvar ansAns (disp workDataTaskOne ansTwo))

(print (/ ansAns (length workDataTaskOne)))

