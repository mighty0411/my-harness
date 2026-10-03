type StatusBadgeProps = {
  className?: string;
  status?: "작성 중";
};

function StatusBadge({ className, status = "작성 중" }: StatusBadgeProps) {
  return (
    <div className={className || "bg-[var(--color\\/canvas,white)] border border-[var(--color\\/hairline,#e0e0e0)] border-dashed content-stretch flex gap-[var(--spacing\\/4,4px)] items-center px-[var(--spacing\\/12,12px)] py-[var(--spacing\\/4,4px)] relative rounded-[var(--radius\\/badge,9999px)]"} data-node-id="23:2">
      <p className="[word-break:break-word] font-['Pretendard:SemiBold'] leading-[1.4] not-italic relative shrink-0 text-[12px] text-[color:var(--color\/text-muted,#707070)] whitespace-nowrap" data-node-id="23:3">
        작성 중
      </p>
    </div>
  );
}

export default function ListRow({ className }: { className?: string }) {
  return (
    <div className={className || "bg-[var(--color\\/canvas,white)] content-stretch flex gap-[var(--spacing\\/12,12px)] items-center px-[var(--spacing\\/16,16px)] py-[var(--spacing\\/12,12px)] relative w-[342px]"} data-node-id="23:26" data-name="list-row">
      <div className="[word-break:break-word] content-stretch flex flex-[1_0_0] flex-col gap-[var(--spacing\/4,4px)] items-start min-w-px not-italic overflow-clip p-[var(--spacing\/0,0px)] relative" data-node-id="23:27" data-name="texts">
        <p className="font-['Pretendard:SemiBold'] leading-[1.5] relative shrink-0 text-[15px] text-[color:var(--color\/ink,#141414)] w-full" data-node-id="23:28">
          자료 제목
        </p>
        <p className="font-['Pretendard:Regular'] leading-[1.4] relative shrink-0 text-[12px] text-[color:var(--color\/text-muted,#707070)] w-full" data-node-id="23:29">
          2026.09.30 · 스킬
        </p>
      </div>
      <StatusBadge className="bg-[var(--color\/canvas,white)] border border-[var(--color\/hairline,#e0e0e0)] border-dashed content-stretch flex gap-[var(--spacing\/4,4px)] items-center px-[var(--spacing\/12,12px)] py-[var(--spacing\/4,4px)] relative rounded-[var(--radius\/badge,9999px)] shrink-0" />
    </div>
  );
}
