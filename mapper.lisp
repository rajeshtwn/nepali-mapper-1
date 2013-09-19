;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; @author:Aadesh Neupane
;; @description: Maps the Nepali Word to the corresponding to the
;;               rules described.
;;


;;; Storing The Rules as the Constants
(defvar constlist '(ँ   ं  ा  ि ी  ु   ू  े  ै   ो ौअ आ इ ई उ ऊ ऋ ए ऐ ओ औ क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व स श ष ह))
(defconstant ँ  'N'
    "Chandra Bindu Matches to N.") 
(defconstant ं  'M'
    "...")
(defconstant ा  'AA'
    "...")
(defconstant ि  'IH'
    "...")
(defconstant ी  'IH'
    "...")
(defconstant ु   'UH'
    "...")    
(defconstant ू   'UH'
    "...")
(defconstant े  'EH'
    "...")
(defconstant ै   "AH IH"
    "...")    
(defconstant ो  'OH'
    "...")
(defconstant ौ  "AH UH"
    "...")
(defconstant अ  'AH'
    "...")
(defconstant आ  'AA'
    "...")
(defconstant इ  'IH'
    "...")
(defconstant ई  'IH'
    "...")
(defconstant उ  'UH'
    "...")
(defconstant ऊ  'UH'
    "...")
(defconstant ऋ   "R IH"
    "...")
(defconstant ए  'EH'
    "...")
(defconstant ऐ  "AH IH"
    "...")
(defconstant ओ  'OH'
    "...")
(defconstant औ  "AH UN"
    "...")
(defconstant क  "K AH"
    "...")
(defconstant ख  "KA AH"
    "...")
(defconstant ग  "G AH"
    "...")
(defconstant घ  "GA AH"
    "...")
(defconstant ङ  "NG AH"
    "...")
(defconstant च  "CH AH"
    "...")
(defconstant छ  "CHA AH"
    "...")
(defconstant ज  "JH AH"
    "...")
(defconstant झ  "JHA AH"
    "...")
(defconstant ञ  "N AH"
    "...")
(defconstant ट  "T AH"
    "...")
(defconstant ठ  "TA AH"
    "...")
(defconstant ड  "D AH"
    "...")
(defconstant ढ  "DA AH"
    "...")
(defconstant ण  "N AH"
    "...")
(defconstant त  "TH AH"
    "...")
(defconstant थ  "THA AH"
    "...")
(defconstant द  "DH AH"
    "...")
(defconstant ध  "DHA AH"
    "...")
(defconstant न  "N AH"
    "...")
(defconstant प  "P AH"
    "...")
(defconstant फ  "PA AH"
    "...")
(defconstant ब  "B AH"
    "...")
(defconstant भ  "BA AH"
    "...")
(defconstant म  "M AH"
    "...")
(defconstant य  "Y AH"
    "...")
(defconstant र  "R AH"
    "...")
(defconstant ल  "L AH"
    "...")
(defconstant व  "W AH"
    "...")
(defconstant स  "S AH"
    "...")
(defconstant श  "S AH"
    "...")
(defconstant ष  "S AH"
    "...")
(defconstant ह  "HH AH"
    "...")
(print ं)
(print ी)
(print ै )
(print ह )

;;;Functions that take the file that need to be Mapped
;;(with-open-file (stream "wordlist.txt")
;;    (do ((line (read-line stream nil)
;;               (read-line stream nil)))
;;        ((null line))
;;     (print line)))
      
;;(with-open-file (stream "wordlist.txt")
;;    (do ((char (read-char stream nil)
;;               (read-char stream nil)))
;;        ((null char))
;;      (print char)))      

;;(let ((constantslist '(ँ   ह  ै   ी )))
;;    (print constantslist))
;;(print((list 'ह )))
(print constlist)
