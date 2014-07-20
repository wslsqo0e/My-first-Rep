;;selection with a mouse being immediately injected to the kill ring
(setq mouse-drag-copy-region t)

;;smart-compile'
(require-package 'smart-compile)
(global-set-key (kbd "<f5>") 'smart-compile)

;;yasnippet 定义某些缩写词的模板，菜单内可见
;; (require 'yasnippet) ;; not yasnippet-bundle
;;     (yas-global-mode 1)

;; use IPython for python-mode
;;(require-package 'python-mode)
(setq
 python-shell-interpreter "ipython3"
 python-shell-interpreter-args ""
 python-shell-prompt-regexp "In \\[[0-9]+\\]: "
 python-shell-prompt-output-regexp "Out\\[[0-9]+\\]: "
 python-shell-completion-setup-code
   "from IPython.core.completerlib import module_completion"
 python-shell-completion-module-string-code
   "';'.join(module_completion('''%s'''))\n"
 python-shell-completion-string-code
   "';'.join(get_ipython().Completer.all_completions('''%s'''))\n")

;;some customer key-bindings
(global-set-key (kbd "C-z") 'undo)
;;disable cua-mode in org-mode, because of some key-binding conflicts.
(add-hook 'org-mode-hook
          (lambda ()
            (cua-mode -1)))

(provide 'init-local)
