type ConfirmCheckboxProps = {
  className?: string;
  checked?: "true";
};

function ConfirmCheckbox({ className, checked = "true" }: ConfirmCheckboxProps) {
  return (
    <div className={className || "bg-[var(--color\\/canvas-soft,#f3f3f3)] content-stretch flex gap-[var(--spacing\\/12,12px)] items-center px-[var(--spacing\\/16,16px)] py-[var(--spacing\\/12,12px)] relative rounded-[var(--radius\\/input,16px)] w-[342px]"} data-node-id="23:108">
      <div className="bg-[var(--color\/ink,#141414)] content-stretch flex gap-[var(--spacing\/0,0px)] items-center justify-center overflow-clip p-[var(--spacing\/0,0px)] relative rounded-[var(--radius\/toggle,9999px)] shrink-0 size-[24px]" data-node-id="23:109" data-name="checkbox-box">
        <p className="[word-break:break-word] font-['Pretendard:SemiBold'] leading-[1.4] not-italic relative shrink-0 text-[12px] text-[color:var(--color\/canvas,white)] whitespace-nowrap" data-node-id="23:110">
          ✓
        </p>
      </div>
      <p className="[word-break:break-word] flex-[1_0_0] font-['Pretendard:Regular'] leading-[1.5] min-w-px not-italic relative text-[13px] text-[color:var(--color\/ink,#141414)]" data-node-id="23:111">
        금지 항목(개인정보, 고객정보, 회사기밀, 타인 저작물)이 포함되지 않았음을 확인합니다.
      </p>
    </div>
  );
}
