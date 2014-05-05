filetype off
set nocp
call pathogen#infect()
call pathogen#helptags()
filetype plugin indent on
syntax on
set number
set paste
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
let ropevim_vim_completion = 1
let ropevim_extended_complete = 1
let g:ropevim_autoimport_modules = ["os.*","traceback","django.*", "xml.etree"]
imap <c-space> <C-R>=RopeCodeAssistInsertMode()<CR>
