;;; ellama.el --- Tsubasa configuration -*- lexical-binding: t; -*-
(with-eval-after-load 'ellama
  (require 'llm-openai)
  (dolist (entry '(("Tsubasa Fast" . "tsubasa-fast")
                   ("Tsubasa Pro" . "tsubasa-pro")))
    (setf (alist-get (car entry) ellama-providers nil nil #'equal)
          (make-llm-openai-compatible
           :url "https://api.tsubasa.sh/v1/"
           :key (lambda () (or (getenv "TSUBASA_API_KEY")
                              (user-error "Set TSUBASA_API_KEY before using Tsubasa")))
           :chat-model (cdr entry)
           :embedding-model nil
           :default-chat-max-tokens 4096))))
