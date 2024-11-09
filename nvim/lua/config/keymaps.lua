-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

vim.keymap.set(
  "n",
  "<leader>e",
  ":lua require('oil').open()<CR>",
  { noremap = true, silent = true, desc = "Open Oil.nvim" }
)
