-- Permet à LaTeX de couper les chemins et autres fragments de code en ligne
-- lorsqu'ils sont trop longs pour tenir sur une ligne du PDF.
function Code(element)
  if FORMAT:match("latex") then
    local escaped = element.text:gsub("([%%#{}])", "\\%1")
    return pandoc.RawInline("latex", "\\nolinkurl{" .. escaped .. "}")
  end
end
